from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

df = px.data.gapminder()
fig = px.line(df.query("country == 'Sweden'"), x = "year", y = "pop")

slider_value = 20
selected_fruit = "apple"
number1 = 0
number2 = 0
sum_calculate = number1 + number2

def perform_calculation(state):
    print(state.sum_calculate)

    state.sum_calculate = int(state.number1) + int(state.number2)

def clear_results(state):
    state.sum_calculate = ""

with tgb.Page() as page:
    with tgb.part(class_name="container"):
        with tgb.layout(columns="1 1 1"):
            with tgb.part() as column_fruit:
                tgb.text("# Hello there Taipy", mode="md")
                tgb.text("Welcome to the world of reactive programming!")

                # binds to slider value variable and makes it dynamic
                tgb.slider(value="{slider_value}", min=1, max=100, step=5)
                tgb.text("Slider value is at {slider_value}")

                tgb.text("Select your favourite fruit:", mode="md")
                tgb.selector(
                    value="{selected_fruit}",
                    lov=["apple", "banana", "tomato", "avocado"],
                    dropdown=True,
                )
                tgb.text("Yummy yummy {selected_fruit}")
                tgb.image("assets/{selected_fruit}.jpg")

            with tgb.part() as column_calculator:
                tgb.text("Cool Calculator", mode="md")

                # on_change = function will run when value is changed
                tgb.text("Type in a number:")
                tgb.input("{number1}", on_change=clear_results)

                tgb.text("Type in another number:")
                tgb.input("{number2}", on_change=clear_results)

                tgb.text("You have typed in {number1} and {number2}")

                # on_action = function will run when button is pressed
                tgb.button("CALCULATE", class_name="plain", on_action=perform_calculation)

                tgb.text("{number1} + {number2} = {sum_calculate}")

            with tgb.part() as column_data:
                tgb.table("{df}", page_size=20)
                tgb.chart(figure="{fig}")


if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)
