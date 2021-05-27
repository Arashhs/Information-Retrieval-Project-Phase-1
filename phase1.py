import ir_algorithms

file_name = 'IR_Spring2021_ph12_7k.xlsx'

def main():
    ir_system = ir_algorithms.IR()
    ir_system.build_inverted_index(file_name)



if __name__ == '__main__':
    main()