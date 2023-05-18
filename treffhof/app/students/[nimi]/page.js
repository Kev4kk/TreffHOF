"use client"
import Image from 'next/image';
import styles from '../../page.module.css';
import Header from "../../header.js";
import 'bootstrap/dist/css/bootstrap.css';
import '../../globals.css';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import MainimisteTabel from "../../mainimisteTabel.js";



export default function Page({ params }) {
  const [top50stu, setTop50stu] = useState([]);
  const [data, setData] = useState({mentions:[]});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("/mentions.json");
        const data1 = await response1.json();
        setData(data1[params.nimi]);
        console.log(data1[params.nimi]);
      } catch (error) {
        console.error('Error loading JSON files:', error);
      }
    };

    fetchData();
  }, []);



  return (
    <>
      <Header />
      <main className={styles.main}>
        <div className={styles.content}>
          <div className={styles.titles}>
          </div>
          <div className={styles.topid}>
            <div className={styles.vasakÕpilased}>
              {(top50stu !== {}) ? (
                <>
                <h1 className={styles.subsubtitle}><u>{data.nimi}</u></h1>
              
                <p>Mainimisi kokku: {data.summa}</p>
                <p>Koht: {parseInt(params.nimi)+1}</p>
                
                
                <MainimisteTabel data={data.mentions}/>

                </>
              ) : (
                <p>Laen...</p>
              )}
            </div>

          </div>
        </div>
        <footer className="bg-dark text-light text-center py-3" style={{width: "100%"}}>
          <div className="container">
            <p className="mb-0">Credit: Kevin Akkermann ja Toomas Herodes (B20)</p>
          </div>
        </footer>
      </main>
    </>
  )
}
