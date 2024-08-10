# Home Sweet Home 🏠
"Home Sweet Home" is a comprehensive web application designed to empower users to interactively explore, analyze, and predict real estate data. Whether you're a potential buyer, seller, or simply curious about the real estate market, this platform provides valuable insights and tools to support your decision-making process.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
  
## Introduction
In today's dynamic real estate market, making informed decisions is crucial. Home Sweet Home is your go-to solution for understanding property trends, estimating property values, and exploring the market with interactive data visualizations. This tool is perfect for anyone involved in real estate, from first-time homebuyers to seasoned investors.

## Features
- **Interactive Data Visualization**: Gain insights from a variety of charts and graphs including scatter mapbox, word cloud, scatter plot, pie chart, box plot, and distplot.
- **Price Prediction**: Predict house and flat prices based on user input and analysis of similar properties.
- **Area Analysis**: Analyze any specific area in depth, helping users make well-informed decisions.
- **Real-Time Data**: Utilize up-to-date data to reflect current market conditions.

## Installation
Follow these steps to get a copy of the project running on your local machine.

### Prerequisites
- Python 3.12+
- pip (Python package installer)
- Virtualenv (Optional but recommended)
### Installation Steps
1. Clone the repository:

    `git clone https://github.com/22Ranjan15/House-Flat_Price_Prediction.git`
   
    `cd House-Flat_Price_Prediction`

3. Create and activate a virtual environment (optional but recommended):

    - Create virtual environment: `python3 -m venv venv`
   
    - Activate virtual environment on Windows: `venv\Scripts\activate`

4. Install the required packages:

    `pip install -r requirements.txt`

5. Run the application:

    `streamlit run 1_Home.py`

6. To access the web application open your browser and go to [application](https://22ranjan15-house-flat-price-prediction-1-home-snz2tr.streamlit.app/).

## Usage
1. **Explore Data**: Use the interactive charts and maps to explore different aspects of the real estate market.
2. **Predict Prices**: Input specific property details to get a predicted market value.
3. **Analyze Areas**: Enter an area of interest to get a detailed analysis including price trends and similar properties.
     
## Technologies Used
- **Frontend & Backend**: Python, Streamlit
- **Data Visualization**: Plotly, Matplotlib, Seaborn
- **Machine Learning Libraries**: Scikit-learn, Pandas, NumPy
- **Deployment**: Streamlit Cloud
  
## Project Structure
`REAL STATE MODEL/`  
`├── __pycache__/`  
`├── Datasets/`  
`├── Demo/`  
`├── myenv/`  
`├── pages/`  
`│   ├── 2_Price_Predictor.py`  
`│   ├── 3_Analysis_Page.py`  
`│   ├── 4_Apartment_Recommendation.py`  
`├── .gitattributes`  
`├── .gitignore`  
`├── 1_Home.py`  
`├── git_lfs.txt`  
`├── pipeline.pkl`  
`├── README.md`  
`└── requirements.txt`  

## Contributing
Contributions are welcome! If you have suggestions, bug reports, or want to contribute to the code, please create an issue or submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
   
## License
This project is licensed under the MIT License.

## Contact
For any inquiries, feel free to reach out:

- **GitHub**: [22Ranjan15](https://github.com/22Ranjan15)
- **Email**: [Mail Here](msd23012@iiitl.ac.in)
