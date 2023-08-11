# Pico y Placa Predictor

The **Pico y Placa** predictor is a Python program designed to help users determine whether a vehicle with a given license plate can be driven on the road during certain hours based on the Pico y Placa regulations. This program is a command-line tool that provides predictions according to the license plate, date, and time provided by the user.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the repository's directory.

3. Run the program by executing the following command:

```bash
python pico_placa.py
```

4. Follow the prompts to input the license plate, date, and time. The program will then provide you with information about whether you can drive during the specified time.

### Running the Tests

1. Run the unit tests by executing the following command:

```bash
python -m unittest test_pico_placa.py
```


## Clean Code and Object-Oriented Design

The Pico y Placa predictor code adheres to clean code and object-oriented design principles. Some of the key features that demonstrate these principles include:

- **Modularization:** The code is organized into a class-based structure where each method serves a specific purpose. This enhances code maintainability and readability.

- **Encapsulation:** Methods are designed to encapsulate specific functionalities, which improves code reusability and isolates concerns.

- **Validation:** The code includes input validation for license plates, date formats, and time formats, ensuring that only valid input is processed.

- **Separation of Concerns:** The code separates different aspects of the prediction process into separate methods, making it easier to understand and modify specific parts of the functionality.

- **Unit Testing:** The unit tests cover various scenarios to ensure the correctness of the program's logic. This promotes code reliability and robustness.

- **Descriptive Variable and Method Names:** Descriptive variable and method names make the code self-explanatory, enhancing readability and understanding.
