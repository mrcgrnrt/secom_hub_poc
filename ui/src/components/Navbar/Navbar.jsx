import { IfxNavbar, IfxNavbarItem, IfxSearchBar } from '@infineon/infineon-design-system-react';
import React, { useState } from 'react';
import { IfxNavbarProfile } from '@infineon/infineon-design-system-react';
import './navbar.scss';

function Navbar() {
  
  const [userName] = useState("");
  const [userNameShort] = useState("");

  return (
    <IfxNavbar  show-logo-and-appname="true" application-name="SECoM Hub" fixed="false" logo-href="/" logo-href-target="_self">
      <IfxNavbarItem href="/" target="_self" slot="left-item" icon="" show-label="true">
        Sensors
      </IfxNavbarItem>
      <IfxNavbarItem href="/" target="_self" slot="left-item" icon="" show-label="true">
        Configuration
      </IfxNavbarItem>
  
      <IfxSearchBar slot="search-bar-left" is-open="false"></IfxSearchBar>
    
      <IfxNavbarProfile user-name={userName} slot="right-item" image-url={userNameShort} show-label="true" href="" target="_blank"></IfxNavbarProfile>
    </IfxNavbar>
  );
}

export default Navbar;