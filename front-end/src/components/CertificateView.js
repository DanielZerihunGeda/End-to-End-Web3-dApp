// CertificateView.js

import React, { useState } from 'react';

const CertificateView = () => {
  const [assetId, setAssetId] = useState('');
  const [certificateDetails, setCertificateDetails] = useState(null);

  const handleSearch = async () => {
    // Implement logic to fetch certificate details by asset ID from the backend
    try {
      // Dummy data for demonstration purposes, replace with actual API call
      const dummyData = {
        traineeName: 'John Doe',
        completionDate: '2024-01-15',
        // Add more details as needed
      };

      setCertificateDetails(dummyData);
    } catch (error) {
      console.error('Error fetching certificate details:', error);
    }
  };

  return (
    <div
      style={{
        background: '#f8f8f8', // Light gray background color
        height: '100vh', // Full height of the viewport
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
      }}
    >
      <div
        style={{
          background: '#fff', // White background color for the box
          padding: '20px',
          borderRadius: '8px',
          boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)', // Light shadow for depth
          maxWidth: '400px', // Limiting the width of the box
        }}
      >
        <h1 style={{ color: 'red', fontSize: '24px', marginBottom: '20px' }}>10 Academy Certificate</h1>

        <div style={{ margin: '20px 0' }}>
          <label style={{ marginRight: '10px' }}>Enter Asset ID:</label>
          <input
            type="text"
            value={assetId}
            onChange={(e) => setAssetId(e.target.value)}
            style={{ padding: '10px', borderRadius: '4px', border: '1px solid #ccc', marginRight: '10px' }}
          />
          <button
            onClick={handleSearch}
            style={{
              padding: '10px 15px',
              backgroundColor: 'red',
              color: 'white',
              borderRadius: '4px',
              border: 'none',
              cursor: 'pointer',
            }}
          >
            Search
          </button>
        </div>

        {certificateDetails && (
          <div>
            <h2>Certificate Details</h2>
            <p>
              Trainee Name: {certificateDetails.traineeName}
              <br />
              Completion Date: {certificateDetails.completionDate}
              {/* Add more details as needed */}
            </p>
          </div>
        )}
      </div>

      <div style={{ marginTop: '30px', fontStyle: 'italic', fontSize: '14px' }}>
        <p>Developed by: Daniel Zerihun</p>
        <p>2024 Year Calendar</p>
        {/* Add your 2024 calendar content here */}
      </div>
    </div>
  );
};

export default CertificateView;
