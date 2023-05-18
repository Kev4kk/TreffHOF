"use client"
import Image from 'next/image';
import styles from '../../page.module.css';
import Header from "../../header.js";
import 'bootstrap/dist/css/bootstrap.css';
import '../../globals.css';
import React, { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Page({ params }) {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response1 = await fetch("/klassMentions.json");
        const data1 = await response1.json();
        console.log(data)
        setData(data1[params.nimi]);
        console.log("DATA: ")
        console.log(data1[params.nimi]);
        console.log(data);
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
              {(data != {}) ? (
                <>
                  <h3 className={styles.subsubtitle}><u>{data.aasta}</u></h3>
                  <p>Koht: {parseInt(params.nimi)+1}</p>

                  <table className={styles.table}>
                    <thead>
                      <tr>
                        <th>#</th>
                        <th>Õpilane</th>
                        <th>Korrad</th>
                      </tr>
                    </thead>
                    <tbody>
                      {(data["kokku"] != undefined) ? data["kokku"].map((element, index) => (
                        <tr key={index}>
                          <td>{index + 1}</td>
                          <td><Link href={"/students/" + element[2]}><u>{element[0]}</u></Link></td>
                          <td>{element[1]}</td>
                        </tr>

                      )) : (<></>)}
                    </tbody>
                  </table>

                </>
              ) : (
                <p>Laen...</p>
              )}
            </div>

          </div>
        </div>
        <footer className="bg-dark text-light text-center py-3" style={{ width: "100%" }}>
          <div className="container">
            <p className="mb-0">Credit: Kevin Akkermann ja Toomas Herodes (B20)</p>
          </div>
        </footer>
      </main>
    </>
  )
}
