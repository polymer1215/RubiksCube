"""Rubik's Cube Simulator - Main Entry Point"""
from simulator import Simulator


def main():
    """Main function to run the Rubik's Cube simulator."""
    sim = Simulator()

    input("Press Enter to initialize a cube:\n")
    sim.console_render_cube()
    
    raw_moves = input("Enter moves: ")
    sim.carry_raw(raw_moves)
    sim.console_render_cube()
    
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()