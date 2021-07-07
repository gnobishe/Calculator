import calc_model
import calc_view
import calc_controller

# По порядку происходит инициализация всех частей калькулятора:
# 1) модель с расчётными функциями;
# 2) контроллер, связанный с моделью и видом, для отправки данных и вызова расчётных функций;
# 3) вид, связанный с моделью и контроллером, для отображения полученного результата.
if __name__ == '__main__':
    model = calc_model.Model()
    control = calc_controller.Controller(model)
    view = calc_view.View(model, control)
    view.print_result()
