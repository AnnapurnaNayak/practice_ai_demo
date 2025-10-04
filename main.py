from flask import Flask, Response, request, render_template
from fpdf import FPDF
import io
from youtube_api import youtube_search_api  # Make sure this import points to your actual YouTube search function
from captions_module.captions import get_captions       # Replace with your actual captions fetching function


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])


def generate_pdf():
    data = request.json
    user_text = data.get('text', 'Default hardcoded text')

    # Use input text to search YouTube videos
    videos = youtube_search_api(user_text)

    # Create PDF object and page
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add the user search query on top
    pdf.cell(0, 10, f"Search Query: {user_text}", ln=True)

    if videos:
        # For demo, just take the first video and fetch captions
        video = videos[0]

        video_title = video.get('description', 'No Title')
        video_id = video.get('videoId')
        video_url = video.get('url','') 

        # Add video title in bold
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, video_title, ln=True)

        # Add YouTube URL in italics (not clickable but visible)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, video_url, ln=True)

        # Fetch captions for the video
        captions = get_captions(video_id)

        # Add captions or fallback message
        pdf.set_font("Arial", size=12)
        if captions:
            pdf.multi_cell(0, 10, "\n".join(captions))
        else:
            pdf.cell(0, 10, "No captions found.", ln=True)

    else:
        # No videos found fallback
        pdf.cell(0, 10, "No videos found for the query.", ln=True)

    # Output PDF to bytes buffer
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_buffer = io.BytesIO(pdf_bytes)
    pdf_buffer.seek(0)

    # Return PDF as downloadable file
    return Response(
        pdf_buffer,
        mimetype='application/pdf',
        headers={"Content-Disposition": "attachment;filename=output.pdf"}
    )
if __name__ == '__main__':
    app.run(port=5000, debug=True)  