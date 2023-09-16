import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Home`}>
      <HomepageHeader />
      <main>
        <HomepageFeatures />

    Complete package for developing LiPo-powered IoT applications:

    - Speedy processor with tons of flash and RAM, rich peripherals, and native Wi-Fi and Bluetooth
    - Low-current deep-sleep, and even lower-power states
    - Flexible power options and control
    - Charging control and battery montoring
    - Existing expansions for prototyping
      </main>
    </Layout>
  );
}
