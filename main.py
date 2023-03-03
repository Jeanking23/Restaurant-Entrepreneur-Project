from simulation import Simulation

def write_to_file():
    file = open("log.text", "w")
    file.write("simulation")
    file.close()
write_to_file()

process = Simulation()
process.run_simulation( 10)