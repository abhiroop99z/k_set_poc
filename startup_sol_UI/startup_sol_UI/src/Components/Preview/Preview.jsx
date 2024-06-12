import React, { Fragment } from "react";

import styles from "./Preview.module.css";

function Preview() {
  return (
    <Fragment>
      <div className={styles.previewBox}>
        <p>I am a preview box</p>
      </div>
    </Fragment>
  );
}

export default Preview;
