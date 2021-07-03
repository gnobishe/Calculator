import calc_model
import calc_view
import calc_controller

if __name__ == '__main__':
    model = calc_model.Calculator()
    control = calc_controller.Controller(model)
    window = calc_view.Window(model, control)
    window.print_result()
