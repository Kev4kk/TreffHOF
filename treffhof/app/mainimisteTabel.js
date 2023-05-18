"use client"
import HeaderStyles from "./header.module.css"
import { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.css';
import './globals.css';
import styles from './page.module.css';
import Fuse from "fuse.js";
import Link from "next/link";

import React from 'react';
import { Table } from "react-bootstrap";

function MainimisteTabel(props) {
  let data =  Array.from(props.data)
  data.sort((a, b) => {
    const stringA = a[1].toLowerCase();
    const stringB = b[1].toLowerCase();
  
    if (stringA > stringB) {
      return -1;
    }
    if (stringA < stringB) {
      return 1;
    }
    return 0;
  });
  useEffect(() => {console.log(data)})

  return (
    <div>
    <table className={styles.table}>
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Aasta</th>
                    <th>Väljalase</th>
                    <th>Korrad</th>
                    <th>Infoleht</th>
                  </tr>
                </thead>
                <tbody>
                  {data.map((element, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td>{element[1].slice(0,4)}</td>
                      <td>{element[1].split("_")[1].split(".txt")[0]}</td>
                      <td>{element[0]}</td>
                      <td><Link href="#">Link</Link></td>
                    </tr>
                    
                  ))}
                </tbody>
              </table>


    </div>
  );
  
}

export default MainimisteTabel;
