# UTI

## Introduction

UTI stands for **U**r **T**houghts on **I**mages. This Python project leverages GenAI technology to analyze images from marketing campaigns and provide actionable insights. It utilizes object detection capabilities to identify key elements within images and then generates suggestions based on detected objects and user input.

**Features:**

+ Object Detection: Accurately identifies objects within images using advanced GenAI models.
+ Insight Generation: Offers suggestions based on detected objects and user-provided context.
+ User-Friendly Interface: Easy to use and understand, allowing for quick and efficient analysis.

## Usage:

1. Installation:

```Python
git clone https://github.com/What-s-behind/UTI
cd /UTI
pip install -r requirements.txt
```

2. Setup the environment
Then, you are required to get the API key from Gemini and Groq: 
+ [Gemini's API key](https://aistudio.google.com/app/apikey)
+ [Groq's API key](https://console.groq.com/keys)

After that, let's create a `.env` file and follow this format: 
```
GEMINI_API_KEY="GEMINI_API_KEY"
GROQ_API_KEY="GROQ_API_KEY"
```
> We leave the `.env.examples` as a template for implementing our environment. 

3. Running the Application:
Navigate to the project directory in your terminal. Run the following command:

```
streamlit run app.py
```

## Contact Us:
For any questions, feedback, or bug reports, please contact:

+ *Lê Đức Minh* | **LinkedIn:** [/in/minh-le-duc/](https://www.linkedin.com/in/minh-le-duc-a62863172/ ) | **Gmail:** minh.leduc.0210@gmail.com
+ *Lê Nguyễn Đăng Khoa* | **LinkedIn:** [/in/khoale-maiu/](https://www.linkedin.com/in/khoale-maiu/ ) | **Gmail:** khoale.maiu@gmail.com
+ *Trần Ngọc Đại* | **LinkedIn:** [/in/ngoc-dai-tran/](https://www.linkedin.com/in/ngoc-dai-tran-621b62292/) | **Gmail:** ngocdai101004@gmail.com 
+ *Phạm Minh Mẫn* | **LinkedIn:** [/in/man-pham/](https://www.linkedin.com/in/m%E1%BA%ABn-ph%E1%BA%A1m-47b493311/ ) | **Gmail:** phamminhman1312005@gmail.com

## Note:

+ This project is currently under development and may contain some limitations.
+ The accuracy of insights depends on the quality of the image and the context provided.

