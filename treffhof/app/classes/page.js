"use client"
import Image from 'next/image';
import styles from '../page.module.css';
import Header from "../header.js";
import 'bootstrap/dist/css/bootstrap.css';
import '../globals.css';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Home() {
  const [top50stu, setTop50stu] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("/klassMentions.json");
        const data1 = await response1.json();
        setTop50stu(data1);
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
              <h3 className={styles.subsubtitle}><Link href={"/classes/"}><u>Klasside top 50</u></Link></h3>
              {(top50stu !== []) ? (
                <table className={styles.table}>
                  <thead>
                    <tr>
                      <th>#</th>
                      <th style={{ width: "1rem", overflow: "clip", paddingRight: "0.5rem" }}>Lõpetamisaasta + klass</th>
                      <th>Mainimisi</th>
                      <th>Keskmine</th>
                    </tr>
                  </thead>
                  <tbody>
                    {top50stu.map((element, index) => (
                      <tr key={index}>
                        <td>{index + 1}</td>
                        <td><Link href={"/classes/" + index}>{element.aasta}</Link></td>
                        <td>{element.kokku.reduce((partialSum, a) => partialSum + a, 0)}</td>
                        <td>{element.keskmine.toFixed(2)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
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
