// src/CertificateForm.js
import React, { useState } from 'react';
import axios from 'axios';
import './CertificateForm.css'; // Import additional CSS file for styling

const CertificateForm = () => {
  const [formData, setFormData] = useState({
    traineeName: '',
    trainingProgram: '',
    dateOfCompletion: '',
    durationOfTraining: '',
    issuingOrganization: '',
    serialNumber: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const generateCertificateToken = async () => {
    try {
      const response = await axios.post('http://localhost:4001/Generate_NFT', formData);
      console.log(response.data); // handle the response as needed
    } catch (error) {
      console.error('Error generating certificate token:', error);
    }
  };

  return (
    <div className="certificate-form">
      <img src="/logo.png" alt="Logo" className="logo" /> {/* Updated logo reference */}
      <h1 className="form-title">10 Academy</h1>
      <form>
        <div className="form-group">
          <label className="form-label">Trainee's Full Name</label>
          <input type="text" name="traineeName" value={formData.traineeName} onChange={handleInputChange} />
        </div>

        <div className="form-group">
          <label className="form-label">Training Program</label>
          <input type="text" name="trainingProgram" value={formData.trainingProgram} onChange={handleInputChange} />
        </div>

        <div className="form-group">
          <label className="form-label">Date of Completion</label>
          <input type="text" name="dateOfCompletion" value={formData.dateOfCompletion} onChange={handleInputChange} />
        </div>

        <div className="form-group">
          <label className="form-label">Duration of Training</label>
          <input type="text" name="durationOfTraining" value={formData.durationOfTraining} onChange={handleInputChange} />
        </div>

        <div className="form-group">
          <label className="form-label">Name of Issuing Organization</label>
          <input type="text" name="issuingOrganization" value={formData.issuingOrganization} onChange={handleInputChange} />
        </div>

        <div className="form-group">
          <label className="form-label">Serial Number of Certificate</label>
          <input type="text" name="serialNumber" value={formData.serialNumber} onChange={handleInputChange} />
        </div>

        <button type="button" onClick={generateCertificateToken} className="generate-button">
          Generate Certificate Token
        </button>
      </form>
    </div>
  );
};

export default CertificateForm;
