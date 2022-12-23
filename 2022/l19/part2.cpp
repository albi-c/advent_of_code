#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <stdio.h>

#include <glm/glm.hpp>

using Blueprint = std::array<glm::ivec4, 5>;

using CacheKey = std::pair<int, std::array<glm::ivec4, 2>>;

const std::array<glm::ivec4, 4> UNIT_VECTORS = {
    glm::ivec4(1, 0, 0, 0),
    glm::ivec4(0, 1, 0, 0),
    glm::ivec4(0, 0, 1, 0),
    glm::ivec4(0, 0, 0, 1)
};

bool craftable(const glm::ivec4& robot, const glm::ivec4& materials) {
    return robot.x <= materials.x && robot.y <= materials.y &&
           robot.z <= materials.z && robot.w <= materials.w;
}

int find_best(const Blueprint& blueprint, int time, const glm::ivec4& robots, const glm::ivec4& materials, int& earliest_geode) {
   if (time <= 1) {
        return materials.w + robots.w * time;
    }

    if (materials.w) {
        earliest_geode = std::max(earliest_geode, time);
    } else {
        if (time < earliest_geode) {
            return -1;
        }
    }

    if (craftable(blueprint[3], materials)) {
        return find_best(blueprint, time - 1, robots + UNIT_VECTORS[3], materials + robots - blueprint[3], earliest_geode);
    }

    int best = find_best(blueprint, time - 1, robots, materials + robots, earliest_geode);

    if (time == 2) {
        return best;
    }

    bool all_craftable = true;
    for (int i = 0; i < 3; i++) {
        if (!craftable(blueprint[i], robots)) {
            all_craftable = false;
            break;
        }
    }

    if (all_craftable) {
        return best;
    }

    for (int i = 0; i < 3; i++) {
        if (craftable(blueprint[i], materials) && robots[i] <= blueprint[4][i]) {
            best = std::max(
                best,
                find_best(blueprint, time - 1, robots + UNIT_VECTORS[i], materials + robots - blueprint[i], earliest_geode)
            );
        }
    }

    return best;
}

int main() {
    const std::string INPUT = "2022/l19/input.txt";

    std::vector<Blueprint> blueprints;

    FILE* file = fopen(INPUT.c_str(), "r");

    if (!file) {
        std::cerr << "Couldn't open file!\n";
        return 1;
    }

    int index, ore_o, clay_o, obs_o, obs_c, geo_o, geo_ob;
    while (fscanf(
        file,
        "Blueprint %d: "
        "Each ore robot costs %d ore. "
        "Each clay robot costs %d ore. "
        "Each obsidian robot costs %d ore and %d clay. "
        "Each geode robot costs %d ore and %d obsidian.\n",
        &index, &ore_o, &clay_o, &obs_o, &obs_c, &geo_o, &geo_ob
    ) > 0) {
        blueprints.push_back({
            glm::ivec4(ore_o, 0, 0, 0),
            glm::ivec4(clay_o, 0, 0, 0),
            glm::ivec4(obs_o, obs_c, 0, 0),
            glm::ivec4(geo_o, 0, geo_ob, 0),
            glm::ivec4(
                std::max(ore_o, std::max(clay_o, std::max(obs_o, geo_o))),
                obs_c,
                geo_ob,
                0
            )
        });
    }

    int total = 1;
    for (int i = 0; i < 3; i++) {
        int earliest_geode = 0;
        int best = find_best(blueprints[i], 32, glm::ivec4(1, 0, 0, 0), glm::ivec4(0), earliest_geode);
        std::cout << "Blueprint " << (i + 1) << " has score: " << best << "\n";
        if (best < 0) {
            std::cout << "ERROR!\n";
            return 1;
        }
        total *= best;
    }

    std::cout << "Solution: " << total << "\n";

    fclose(file);
}
