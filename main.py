from input.Input import Input
from output.Output import Output

if __name__ == '__main__':
    print("Wallbox Configurator started")
    input_evaluation = Input()
    print("Start input evaluation")
    input_evaluation.start()
    print("Start Display and LED Connection")
    output_evaluation = Output()
    print("Start output evaluation")
    output_evaluation.start()
