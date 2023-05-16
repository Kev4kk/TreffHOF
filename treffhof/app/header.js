"use client"
import HeaderStyles from "./header.module.css"
import { useState } from "react";
import 'bootstrap/dist/css/bootstrap.css';
import './globals.css';

import React from 'react';

function Header() {
  const [searchTerm, setSearchTerm] = useState('');
  
  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <a className="navbar-brand" href="#">TreffHOF</a>
        <form className="d-flex">
          <input className="form-control me-2" type="search" placeholder="Otsi nime:" aria-label="Search" onChange={handleSearch} value={searchTerm}/>
          <button className="btn btn-outline-light" type="submit">Otsi</button>
        </form>
      </div>
    </nav>
  );
}

export default Header;
