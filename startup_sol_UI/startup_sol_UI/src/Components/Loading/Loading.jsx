import React from "react";
import styles from "./Loading.module.css";

function Loading() {
  return (
    <div className={styles.backdrop}>
      <div className={styles.centreDiv}>
        <h1 className={styles.logo}>~Zensar~</h1>
      </div>
    </div>
  );
}

export default Loading;
