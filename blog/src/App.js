import React, {useState} from 'react';
import './App.css';

function App() {
  const [name, setName] = useState('Siddhu!');
  const updateName = async () =>{
    const newName = document.getElementById('name').value;
    setName(newName);
    try{
      const response = await fetch('http://127.0.0.1:3001/submit-name',{
        method:'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify({name:newName}),
    });
    if(response.ok){
      const data = await response.text();
      console.log('from backend'+ data);
    }
    else{
      alert('Error submitting name');
    }
    }
    catch(error){
      alert('Error submitting name');
    }

  };
  return (
    <div className="App">
      <input type="text" id="name"/>
      <button type="submit" onClick={updateName}>Submit</button>
      <h1>Hello {name}!</h1>
    </div>
  );
}

export default App;