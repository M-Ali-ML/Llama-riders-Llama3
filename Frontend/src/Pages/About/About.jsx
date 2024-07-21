import React from "react";
import about from "../../asests/about.png";

const About = () => {
  return (
    <div className="container">
      <div className="col-7 mx-auto mt-4 text-center ">
        <h2 className="h2">Model Specifications</h2>
        <p className="p pt-2">
          This job application assistant is built on state-of-the-art AI
          technology, leveraging advanced algorithms to streamline the
          application process and provide personalized guidance. Below are some
          key features of our design.
        </p>
      </div>

      <div className="col-12 d-flex align-items-center justify-content-between mt-5">
        <div className="boxClr col-2 text-center px-5 py-4 rounded">
          <span className="clr">Llama 3</span> Model
        </div>
        <div className="boxClr col-2 text-center px-5 py-4 rounded">
          <span className="clr">Extensively</span> <br /> Trained
        </div>

        <div className="boxClr col-2 text-center px-5 py-4 rounded">
          <span className="clr">99% </span>Accuracy
        </div>
        <div className="boxClr col-2 text-center px-5 py-4 rounded">
          <span className="clr">High </span>Precision
        </div>
      </div>

      <div className="col-12 mt-5 d-flex align-items-center justify-content-end">
        <div className="col-6">
          <img className="rounded-top" src={about} alt="about" height={500} />
        </div>

        <div className="col-6">
          <div className="aboutText">
            <span>Comprehensive</span>
            <h4>About This Project</h4>
            <p>
              The Job Application Assistant is an AI-powered tool designed to
              streamline job applications by generating personalized responses
              and cover letters. Using a Retrieval-Augmented Generation (RAG)
              framework with a LLaMA 3 model, it integrates information from
              applicants' LinkedIn profiles and resumes to provide tailored
              answers to common job application questions and craft customized
              cover letters. The system extracts key details from the
              applicant’s documents, generates context-aware responses, and
              ensures consistency and quality across applications. This tool
              saves time, increases personalization, and enhances the overall
              efficiency of the job application process.
            </p>
          </div>

          <div className="aboutText mt-5">
            <h4>Technical Team</h4>
            <p>
              <a
                href="https://lablab.ai/event/llama-3-ai-hackathon/llama-riders"
                target="_blank"
                rel="noopener noreferrer"
                className="clr"
              >
                <strong className="clr">"Llama Riders" </strong>
              </a>
              is a dedicated team of five skilled professionals:
              <strong> Mohamed Ali</strong>, Machine Learing Engineer and Team
              Leader,
              <strong> Maryum Sikander</strong>, Data Scientist;
              <strong> Emma Lee</strong>, Python and ML Expert;
              <strong> Sikander Nawaz</strong>, a Full Stack Developer; and
              <strong> Ayush Yadav</strong>, Product Manager. Their project
              leverages the advanced technologies, including JavaScript, Python.
              Using Machine Learning frameworks like TensorFlow and Keras,
              alongside image processing tools OpenCV and PIL, they create
              efficient solutions for medical imaging.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
