from simulator import Simulator

sim = Simulator()

input("enter to initialize a cube:\n")
sim.console_render_cube()
raw = input("moves:")
sim.carry_raw(raw)
sim.console_render_cube()
input()