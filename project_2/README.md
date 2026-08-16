# AI Resume Critiquer

An intelligent resume analysis and feedback tool powered by **Google Gemini AI** and **LangChain**. Upload your resume and receive AI-powered, actionable feedback tailored to your target job role!

## Features

✨ **Key Capabilities:**
- 📄 Support for PDF and TXT resume formats
- 🤖 AI-powered analysis using Google Gemini 2.5 Flash
- 🎯 Job-role-specific feedback (optional)
- 📊 Structured feedback on:
  - Content clarity and impact
  - Skills presentation
  - Experience descriptions
  - Targeted improvements for your job role
  - Missing skills or sections
  - Overall resume quality
  - ATS (Applicant Tracking System) optimization
- 💬 Interactive web interface with Streamlit
- ⚡ Real-time analysis with visual feedback

## Tech Stack

- **Frontend:** Streamlit
- **AI Engine:** Google Gemini 2.5 Flash via LangChain
- **Document Processing:** PyPDF2 (PDF extraction)
- **Environment Management:** python-dotenv
- **Python:** >=3.14

## Installation

### 1. Clone/Navigate to the project:
```bash
cd project_2
```

### 2. Install dependencies:
```bash
python -m pip install -e .
```

This will install:
- Streamlit
- LangChain with Google GenAI
- PyPDF2 (for PDF parsing)
- python-dotenv (for environment variables)

### 3. Set up Google Gemini API:

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_api_key_here
```

## Usage

### Run the Application

```bash
streamlit run src/project_2/__init__.py
```

The app will open in your browser (typically at `http://localhost:8501`).

### How to Use

1. **Upload Resume:** Click the file uploader to select a PDF or TXT file
2. **Target Job Role (Optional):** Enter the job role you're targeting (e.g., "Senior Python Developer", "Product Manager")
3. **Analyze:** Click the "Analyze Resume" button
4. **Review Feedback:** Get detailed, structured feedback with specific recommendations

## Project Structure

```
project_2/
├── README.md                 # This file
├── pyproject.toml            # Project configuration
├── .env                      # Environment variables (API key)
└── src/
    └── project_2/
        └── __init__.py       # Main Streamlit app
```

## How It Works

### Resume Analysis Pipeline

1. **File Upload:** User uploads a resume (PDF or TXT)
2. **Text Extraction:** 
   - PDF: PyPDF2 extracts text from all pages
   - TXT: Direct text reading
3. **AI Analysis:** Google Gemini AI analyzes the resume against:
   - Content quality and clarity
   - ATS optimization
   - Industry best practices
   - Target job role requirements (if provided)
4. **Feedback Generation:** Structured, actionable recommendations are displayed

### Prompt Engineering

The app uses an optimized prompt that guides Gemini to focus on:
- Specific, actionable feedback (not generic advice)
- ATS-friendly improvements
- Job-role-specific enhancements

## Environment Setup

### Google API Key

```bash
# .env file
GOOGLE_API_KEY=your_api_key_here
```

The application uses `python-dotenv` to load the API key at runtime.

## Features Breakdown

### Content Clarity & Impact
- Review how well your accomplishments are communicated
- Suggestions for stronger action verbs and metrics

### Skills Presentation
- Analysis of how skills are showcased
- Alignment with job role requirements

### Experience Descriptions
- Evaluation of bullet points and descriptions
- Recommendations for quantifiable results

### ATS Optimization
- Check for ATS-friendly formatting
- Identify potential parsing issues
- Suggestions for better keyword placement

### Targeted Improvements
- Job-role-specific recommendations
- Industry-relevant skill gaps
- Experience relevance assessment

## Requirements

- Python >=3.14
- Google Gemini API key (free tier available)
- ~50 MB disk space
- Modern web browser for Streamlit UI

## Troubleshooting

**Issue:** "GOOGLE_API_KEY not found"
- **Solution:** Ensure `.env` file exists in the project root with your API key set

**Issue:** "Error occurred: Failed to process PDF"
- **Solution:** Ensure the PDF is not corrupted and contains text (not scanned images)

**Issue:** "Connection timeout"
- **Solution:** Check your internet connection and Google API rate limits

**Issue:** App takes long to analyze
- **Solution:** Large resumes or slow internet may delay analysis. This is normal for the first request.

## Future Enhancements

- 🔄 Batch resume processing
- 📈 Resume score visualization (0-100 scale)
- 🎨 Side-by-side comparison with job descriptions
- 💾 Analysis history and previous feedback
- 📊 Improve sections with AI-powered rewrites
- 🌍 Multi-language resume support
- 📝 Export feedback as PDF report

## API Usage Notes

- The app uses **Gemini 2.5 Flash** model for fast, cost-effective analysis
- Temperature set to 0.7 for balanced creativity and consistency
- Each analysis makes one API call to Google Gemini

## Author

**Sanchali-rif** (sanchalisaha05@gmail.com)

## License

MIT License

---

**Part of the AI Agent Workspace** - A monorepo of AI/ML projects built with Python, LangChain, and modern AI frameworks.
