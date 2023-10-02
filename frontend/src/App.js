import React, { useState, useEffect } from 'react';

function App() {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/energy_resources/')
        .then(response => response.json())
        .then(data => {
            const sortedData = data.sort((a, b) => a.quantity_kw - b.quantity_kw);
            setResources(sortedData);
        });
  }, []);


  return (
    <div className="container">
      <h1>Energy Resources</h1>
      {resources.map(resource => (
        <div key={resource.id}>
          {resource.name} - {resource.type} - £{resource.price_per_kw}/kW - {resource.location} - {resource.quantity_kw} kW
        </div>
      ))}
    </div>
  );
}

export default App;
