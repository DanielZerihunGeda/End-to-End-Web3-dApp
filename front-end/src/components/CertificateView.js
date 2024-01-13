// src/CertificateForm.js
import React, { useState } from 'react';
import axios from 'axios';

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
      <h1 style={{ backgroundColor: 'red', color: 'white', textAlign: 'center' }}>10 Academy</h1>
      <form>
        <label>
          Trainee Name:
          <input type="text" name="traineeName" value={formData.traineeName} onChange={handleInputChange} />
        </label>
        {/* Add similar input fields for other parameters */}
        <button type="button" onClick={generateCertificateToken}>
          Generate Certificate Token
        </button>
      </form>
    </div>
  );
};

export default CertificateForm;
