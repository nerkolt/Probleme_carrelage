# Recursive Tiling Problem

## Project Overview

This project addresses the **Recursive Tiling Problem**, where a chessboard of size \( n \times n \) (with \( n = 2^k \) and \( k \geq 1 \)) contains exactly one defective tile. The objective is to cover the entire board using L-shaped tiles while avoiding the defective tile.

The solution leverages the **divide-and-conquer** approach to recursively break down the problem into smaller subproblems, ultimately leading to a complete tiling solution. The program includes visualization tools to display the initial and final states of the chessboard.

---

## Problem Description

### Specifications

- The input is a chessboard of size \( n \times n \), where \( n \) is a power of 2.
- One tile on the chessboard is defective (marked as unusable).
- L-shaped tiles are used to cover the board. Each L-shaped tile consists of three connected squares.

### Objective

Cover the chessboard completely with L-shaped tiles while leaving the defective tile uncovered.

---

## Solution Approach

### Divide and Conquer

1. **Divide:** The chessboard is recursively divided into four equal-sized quadrants.
2. **Add L-Shape:** Place one L-shaped tile at the center to mark three quadrants as "artificially defective" so they match the structure of the original problem.
3. **Recurse:** Repeat the process for each quadrant until the size of the board is \( 2 \times 2 \), which can be directly solved.

### Visualization

The program includes functionality to visualize:
- The initial chessboard with a defective tile.
- The final tiled chessboard.

---

## Features

- Implementation of the recursive algorithm in Python.
- Visualization using libraries such as Tkinter or Matplotlib.
- Clean and modular code for easy adaptation.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/recursive-tiling-problem.git
