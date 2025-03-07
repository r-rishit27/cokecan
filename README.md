# Coke Can Design Optimizer

## 📌 Project Overview
The **Coke Can Design Optimizer** is a Streamlit-based web application that optimizes the design of a cylindrical can by minimizing its material usage while ensuring ergonomic comfort. It uses **scientific computation** and **AI-driven reasoning** to generate the best possible can dimensions.

## GenAI App Demo 

![WhatsApp Image 2025-03-01 at 20 02 01_9e7ce73e](https://github.com/user-attachments/assets/2288b1a6-0a0e-4064-b786-c1e240c1b97c)
![WhatsApp Image 2025-03-01 at 20 02 31_8b213b08](https://github.com/user-attachments/assets/1800adf3-9c67-4067-98a1-878cca0f9c7b)
![WhatsApp Image 2025-03-01 at 20 02 52_aec602f0](https://github.com/user-attachments/assets/57ab5397-8de1-4fa9-9482-c0c2ca3d6c6b)
![WhatsApp Image 2025-03-01 at 20 03 51_c54d8dd9](https://github.com/user-attachments/assets/f2074897-6b00-4eba-8e87-e7bc71eb3c99)




## 🚀 Features
- **Surface Area Minimization**: Uses mathematical optimization to determine the best radius and height for a given volume.
- **AI-Powered Design Insights**: Utilizes Generative AI via Groq API to provide insights on material efficiency, ergonomics, and aesthetics.
- **Dynamic UI/UX**: A user-friendly interface with interactive sliders and result visualization.
- **Mathematical Formulations**: Displays the formulas and calculations involved in the optimization process.
- **Graphical Representation**: Provides a visual depiction of the optimized can shape.

## 🛠️ Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/coke-can-optimizer.git
   cd coke-can-optimizer
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables (create a `.env` file and add your API key):
   ```env
   GROQ_API_KEY=your_api_key_here
   ```
4. Run the Streamlit app:
   ```sh
   streamlit run bot.py
   ```

## 📊 Usage
1. **Enter the minimum can volume** (default: 500 mL).
2. **Adjust the maximum diameter** using the slider.
3. Click **"Optimize Can Design"** to generate optimal dimensions and AI insights.
4. View AI-generated **design recommendations** and **mathematical formulations**.
5. **Analyze the visual representation** of the optimized can shape.

## 🧠 AI Reasoning
The AI model analyzes:
- **Material efficiency**: Minimizing material waste while maintaining structural integrity.
- **Ergonomics**: Ensuring ease of grip and stability.
- **Manufacturing feasibility**: Practicality of large-scale production.
- **Branding & Aesthetics**: Maintaining an appealing look for marketing.

## 📌 Future Enhancements
- Integration with **3D visualization tools** for better representation.
- Support for **custom materials** to evaluate environmental impact.
- Additional AI-driven **cost and sustainability analysis**.

## 🤝 Contribution
Feel free to open issues and submit pull requests!

🔧 *Developed with Python, Streamlit, SciPy, Matplotlib, and Groq AI*.
