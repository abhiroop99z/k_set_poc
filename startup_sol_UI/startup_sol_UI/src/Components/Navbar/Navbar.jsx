import React from "react";
// import "./Navbar.css";
import styles from "./Navbar.module.css";
// import ZensarLogo from '../../../public/ZensarLogo';

function Navbar() {
  return (
    <div className={styles.topNavbar}>
      <div className={styles.containerFluid}>
        <nav className="navbar navbar-default" id={styles.topNav}>
          {/* <a>ZenVault</a> */}
          <img src="./images/ZnesarLogo.png" alt="Logo" />
          {/* <img
            src="./images/ZenVault_logo.png"
            alt="Logo"
            className = {styles.ZenvaultLogo}
            style={{ height: "100%"}}
          /> */}
        </nav>
      </div>
    </div>
  );
}

export default Navbar;
