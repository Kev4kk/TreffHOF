"use client"
import Image from 'next/image';
import styles from '../../page.module.css';
import Header from "../../header.js";
import 'bootstrap/dist/css/bootstrap.css';
import '../../globals.css';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Page({ params }) {
  const [top50stu, setTop50stu] = useState([]);
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("/klassMentions.json");
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
          <h1 className={styles.title}>HTG Hall Of Fame</h1>
          <h2 className={styles.subtitle}>Vaata, kui palju on sind infolehes mainitud</h2>
          </div>
          <div className={styles.topid}>
            <div className={styles.vasakÕpilased}>
              {(top50stu !== {}) ? (
                <>
                <h3 className={styles.subsubtitle}><u>{data.aasta}</u></h3>
              
                <p>{data.summa}</p>
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
