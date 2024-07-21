import React from "react";
import first from "../../asests/first.png";
import { Link } from "react-router-dom";

const LandingPage = () => {
  return (
    <div className="main d-flex col-lg-12 mt-3 container-fluid px-4">
      <div className="firstCell col-6 d-flex align-items-center">
        <div className="firstCellText col-9">
          <p className="p">Proudly Presenting Job Application Assistant</p>
          <h1 className="mb-4">
            Work Smarter, <br /> Not Harder
          </h1>
          <p>
            Effortless Applications, Impactful Results: Simplify your job search
            with our AI assistant and unlock new career opportunities.
          </p>
          <button className="button px-3 py-1 rounded me-3">
            <Link to="https://llama-riders-job-assistance.streamlit.app/">
              Test Model
            </Link>
          </button>

          <button className="buton px-3 py-1 rounded">
            <a
              className="decoration"
              href="https://github.com/MightyStud/Llama-riders-Llama3"
              target="blank"
            >
              Get Code
            </a>
          </button>
        </div>
      </div>

      <div className="secondCell col-6 d-flex align-items-center justify-content-end">
        <img
          className="rounded image-fluid"
          src={first}
          alt="img"
          height={520}
        />
      </div>
    </div>
  );
};

export default LandingPage;
