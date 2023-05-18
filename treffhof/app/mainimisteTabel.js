"use client"
import HeaderStyles from "./header.module.css"
import { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.css';
import './globals.css';
import styles from './page.module.css';
import Fuse from "fuse.js";


import React from 'react';
import { Table } from "react-bootstrap";

function MainimisteTabel(props) {
  let data =  Array.from(props.data)
  useEffect(() => {console.log(data)})

  return (
    <div>
    <table className={styles.table}>
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Aasta</th>
                    <th>Korrad</th>
                    <th>Infoleht</th>
                  </tr>
                </thead>
                <tbody>
                  {data.map((element, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td>{element[1].slice(0,4)}</td>
                      <td>{element[0]}</td>
                      <td>Link</td>
                    </tr>
                    
                  ))}
                </tbody>
              </table>


    </div>
  );
  
}

export default MainimisteTabel;
