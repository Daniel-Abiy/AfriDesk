# AfriDesk 🌍

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.herokuapp.com/)

AfriDesk is an AI-powered platform designed to help African citizens navigate government services with ease. The application provides clear information about government procedures, office locations, required documents, and more, making it easier for citizens to access essential services.

## Features

- **Government Services Directory**: Browse and search for various government services across different categories
- **Office Locations**: Find government offices with interactive maps and detailed information
- **AI Assistant**: Get answers to your questions about government procedures and requirements
- **Multi-country Support**: Access information for multiple African countries
- **Mobile-friendly**: Responsive design works on all devices

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for the AI assistant functionality)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/afridesk.git
   cd afridesk
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

## How to Use

1. **Home**: Get an overview of available services and quick access to common tasks
2. **Government Services**: Browse services by category or search for specific services
3. **Office Locations**: Find government offices using interactive maps
4. **Ask Questions**: Chat with the AI assistant to get help with government-related queries

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/)
- Icons by [Font Awesome](https://fontawesome.com/)
