"use client"
import HeaderStyles from "./header.module.css"
import { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.css';
import './globals.css';
import Fuse from "fuse.js";


import React from 'react';

function Header() {
  const [top50stu, setTop50stu] = useState([]);
  const [top50tea, setTop50tea] = useState([]);
  const [top50cla, setTop50cla] = useState([]);
  const [topResults, setTopResults] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedOptionIndex, setSelectedOptionIndex] = useState(-1);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const handleKeyDown = (event) => {
    if (event.key === "ArrowDown") {
      event.preventDefault();
      setSelectedOptionIndex((prevIndex) => (prevIndex < topResults.length - 1 ? prevIndex + 1 : prevIndex));
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setSelectedOptionIndex((prevIndex) => (prevIndex > 0 ? prevIndex - 1 : prevIndex));
    }
  };
  
  const handleKeyUp = (event) => {
    if (event.key === "Enter" && selectedOptionIndex >= 0 && selectedOptionIndex < topResults.length) {
      const selectedOption = topResults[selectedOptionIndex];
      // Perform the action for the selected option, e.g., navigate to the selected page
      window.location.href = selectedOption.index < top50stu.length ?
        "/students/" + selectedOption.index :
        "/teachers/" + (selectedOption.index - top50stu.length);
    }
  };
  

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("/mentions.json");
        const data1 = await response1.json();
        setTop50stu(data1);

        const response2 = await fetch("/teacherMentions.json");
        const data2 = await response2.json();
        setTop50tea(data2);

        const response3 = await fetch("/klassMentions.json");
        const data3 = await response3.json();
        setTop50cla(data3);
      } catch (error) {
        console.error('Error loading JSON files:', error);
      }
    };

    fetchData();
  }, []);

  const goToTopResult = (event) => {
    event.preventDefault();
    if (selectedOptionIndex === -1 && topResults.length > 0) {
      const topResult = topResults[0];
      navigateToResult(topResult);
    }
  }

  const navigateToResult = (result) => {
    const targetURL = result.index < top50stu.length ? "/students/" + result.index : "/teachers/" + (result.index - top50stu.length);
    window.location.href = targetURL;
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
    
    if (event.target.value === "") {
      setSearchTerm([]);
      setTopResults([]);
      return;
    }

    console.log("Õpilasi: " + top50stu.length)

    const fuse = new Fuse(top50stu.map(item => {
      const {aasta, ...rest} = item;
      return rest;
    }).concat(top50tea).concat(top50cla), {
      keys: ["nimi", "aasta"]
    });
    
    const results = fuse.search(event.target.value);
    console.log(results[0])
    setTopResults(results.slice(0, 5).map((result) => ({ data: result.item, index: result.refIndex })));

  };
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <a className="navbar-brand" href="/">TreffHOF</a>
        <div className="position-relative">
          <form className="d-flex">
            <input className="form-control me-2" type="search" placeholder="Otsi nime või klassi:" aria-label="Search" onChange={handleSearch} value={searchTerm} onKeyDown={handleKeyDown} onKeyUp={handleKeyUp}/>
            <button className="btn btn-outline-light" type="submit" onClick={goToTopResult}>Otsi</button>
          </form>
          {topResults.length > 0 && (
            <div className="dropdown-menu show" style={{ position: 'absolute', top: '100%', left: 0, marginTop: '0.5rem', zIndex: 1 }}>
              {topResults.map((result, i) => (
                <a key={result.id} className={`dropdown-item ${selectedOptionIndex === i ? "active" : ""}`} 
                  href={result.index < top50stu.length ? "/students/" + result.index : 
                       (result.index < top50stu.length + top50tea.length) ? "/teachers/" + (result.index - top50stu.length) : 
                        "/classes/" + (result.index - top50stu.length - top50tea.length)}>

                    {(result.data.nimi != undefined) ? result.data.nimi : result.data.aasta}
                </a>
              ))}
            </div>
          )}
        </div>
      </div>
    </nav>
  );
  
  
  
  
}

export default Header;
