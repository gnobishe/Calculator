import calc_model
import calc_view
import calc_controller

if __name__ == '__main__':
    model = calc_model.Model()
    control = calc_controller.Controller(model)
    view = calc_view.View(model, control)
