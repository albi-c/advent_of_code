#include <array>
#include <cstddef>
#include <exception>
#include <fstream>
#include <fmt/core.h>
#include <iostream>
#include <glm/glm.hpp>
#include <string>
#include <vector>
#include <unordered_set>
#include <glm/gtx/hash.hpp>
#include <algorithm>

const std::array<glm::ivec2, 4> DIRECTIONS = {{
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}
}};

glm::ivec2 size;
glm::ivec2 destination;
std::vector<std::string> lines;

glm::ivec2 get_direction(const char ch) {
    switch (ch) {
        case '<': return {-1, 0};
        case '>': return {1, 0};
        case 'v': return {0, 1};
        case '^': return {0, -1};
        default:
            fmt::print("Invalid direction: '{}'\n", ch);
            std::terminate();
            return {0, 0};
    }
}

std::size_t pathfind(const glm::ivec2 pos, std::unordered_set<glm::ivec2>& seen, const std::size_t distance, const bool disable_slopes) {
    if (pos.x < 0 || pos.y < 0 || pos.x >= size.x || pos.y >= size.y) {
        return 0;
    }

    const char ch = lines[pos.y][pos.x];

    if (ch == '#' || seen.find(pos) != seen.end()) {
        return 0;
    }

    if (pos == destination) {
        return distance;
    }

    std::size_t m = 0;
    seen.insert(pos);
    if (disable_slopes || ch == '.') {
        for (const auto d : DIRECTIONS) {
            m = std::max(m, pathfind(pos + d, seen, distance + 1, disable_slopes));
        }
    } else {
        m = pathfind(pos + get_direction(ch), seen, distance + 1, disable_slopes);
    }
    seen.erase(pos);
    return m;
}

std::size_t pathfind_wrapper(const bool disable_slopes) {
    std::unordered_set<glm::ivec2> seen;
    return pathfind({1, 0}, seen, 0, disable_slopes);
}

int main() {
    const std::string INPUT = "2023/l23/input.txt";

    std::ifstream file(INPUT);

    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(std::move(line));
    }

    size = {lines[0].size(), lines.size()};
    destination = size - glm::ivec2{2, 1};


    fmt::print("{}\n", pathfind_wrapper(false));
    fmt::print("{}\n", pathfind_wrapper(true));
}
