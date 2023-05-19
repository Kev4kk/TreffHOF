"use client"
import Image from 'next/image';
import styles from './page.module.css';
import Header from "./header.js";
import 'bootstrap/dist/css/bootstrap.css';
import './globals.css';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Home() {
  const [top50stu, setTop50stu] = useState([]);
  const [top50cla, setTop50cla] = useState([]);
  const [top50tea, setTop50tea] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("./mentions.json");
        const data1 = await response1.json();
        setTop50stu(data1.slice(0, 50));

        const response2 = await fetch("./teacherMentions.json");
        const data2 = await response2.json();
        setTop50tea(data2.slice(0, 50));

        const response3 = await fetch("./klassMentions.json");
        const data3 = await response3.json();
        setTop50cla(data3.slice(0, 50));
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
              <h3 className={styles.subsubtitle}><Link href="/students"><u>Õpilaste top 50</u></Link></h3>
              <table className={styles.table}>
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Nimi</th>
                    <th style={{ width: "1rem", overflow: "clip" }}>Lõpuaasta + klass</th>
                    <th>Mainimisi</th>
                  </tr>
                </thead>
                <tbody>
                  {top50stu.map((element, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td><Link href={"/students/" + index}><u>{element.nimi}</u></Link></td>
                      <td>{element.aasta}</td>
                      <td>{element.summa}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className={styles.keskelKlassid}>
              <h3 className={styles.subsubtitle}><Link href="/classes"><u>Klasside top 50</u></Link></h3>
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
                  {top50cla.map((element, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td><Link href={"/classes/" + index}><u>{element.aasta}</u></Link></td>
                      <td>{element.kokku.reduce((partialSum, a) => partialSum + a[1], 0)}</td>
                      <td>{element.keskmine.toFixed(2)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className={styles.paremÕpetajad}>
              <h3 className={styles.subsubtitle}><Link href="/teachers"><u>Õpetajate top 50</u></Link></h3>
              <table className={styles.table}>
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Nimi</th>
                    <th>Mainimisi</th>
                  </tr>
                </thead>
                <tbody>
                  {top50tea.map((element, index) => (
                    <tr key={index}>
                      <td>{index + 1}</td>
                      <td><Link href={"/teachers/" + index}><u>{element.nimi}</u></Link></td>
                      <td>{element.summa}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <footer className="bg-dark text-light text-center py-3" style={{width: "100%"}}>
          <div className="container">
            <p className="mb-0" style={{color: "#BBB"}}>Kogu info ei pruugi olla korrektne</p>
            <p className="mb-0"><Link href="https://github.com/Kev4kk/TreffHOF"><u>Credit</u></Link>: Kevin Akkermann B20</p>
          </div>
        </footer>

      </main>
    </>
  )
}
