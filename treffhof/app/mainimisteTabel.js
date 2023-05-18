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
  const [Data, setData] = useState([])

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

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("/urls.json");
        const data1 = await response1.json();
        setData(data1);
      } catch (error) {
        console.error('Error loading JSON files:', error);
      }
    };

    fetchData();
  }, []);

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
                      <td><Link href={Data["infolehed4/" + element[1]]} target="_blank"><u>Link</u></Link></td>
                    </tr>
                    
                  ))}
                </tbody>
              </table>


    </div>
  );
  
}

export default MainimisteTabel;
