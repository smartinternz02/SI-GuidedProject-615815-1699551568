from flask import Flask, render_template, request
import pickle as pkl

app = Flask(__name__)


# Define the labels for the text input fields
fields = ['team', 'targeted productivity', 'smv', 'wip', 'over time', 'incentive',
       'idle time', 'idle men', 'no of style change', 'no of workers', 'month',
       'quarter Quarter1', 'quarter Quarter2', 'quarter Quarter3',
       'quarter Quarter4', 'quarter Quarter5', 'department finishing',
       'department finishing ', 'department sweing', 'day Monday',
       'day Saturday', 'day Sunday', 'day Thursday', 'day Tuesday',
       'day Wednesday']
labels = [f"{fields[i].capitalize()} : " for i in range(len(fields))]


# Initialize an empty list to store user inputs
user_inputs = []
@app.route("/", methods=["GET", "POST"])
async def index():
    global user_inputs
    res = ''
    if request.method == "POST":
        # Get user input from the form
        for label in labels:
            input_value = request.form.get(label)
            user_inputs.append(input_value)

        # Clear the user inputs list for the next submission
        print(user_inputs)
        user_inputs = [float(i) for i in user_inputs]
        
        model = pkl.load(open('model.pkl', 'rb'))
        sample_input = [10.0, 0.7, 21.82, 1653.0, 6240.0, 0.0, 0.0, 0.0, 2.0, 52.0, 2.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        # prediction = model.predict([sample_input])
        prediction = model.predict([user_inputs])
        res = f"{round(prediction[0]*100, 2)} %"
        print(prediction[0])
        user_inputs = []

        # Display a success message
        message = "Inputs submitted successfully!"

    else:
        message = None

    return render_template("index.html", labels=labels, user_inputs=user_inputs, message=message, prediction=res)

if __name__ == "__main__":
    app.run(debug=True)
