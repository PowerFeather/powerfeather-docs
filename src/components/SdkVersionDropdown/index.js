import React from 'react';
import {useHistory, useLocation} from '@docusaurus/router';
import {
  useActiveDocContext,
  useVersions,
} from '@docusaurus/plugin-content-docs/client';
import {useDocsPreferredVersion} from '@docusaurus/theme-common';
import styles from './styles.module.css';

const getVersionMainDoc = (version) =>
  version.docs.find((doc) => doc.id === version.mainDocId);

export default function SdkVersionDropdown() {
  const versions = useVersions('sdk');
  const activeDocContext = useActiveDocContext('sdk');
  const {savePreferredVersionName} = useDocsPreferredVersion('sdk');
  const history = useHistory();
  const {search, hash} = useLocation();

  if (!activeDocContext?.activeVersion) {
    return null;
  }

  const options = versions.map((version) => {
    const versionDoc =
      activeDocContext.alternateDocVersions[version.name] ??
      getVersionMainDoc(version);

    return {
      name: version.name,
      label: version.label,
      path: `${versionDoc.path}${search}${hash}`,
    };
  });

  const handleChange = (event) => {
    const next = options.find((option) => option.name === event.target.value);
    if (!next) {
      return;
    }

    savePreferredVersionName(next.name);
    history.push(next.path);
  };

  return (
    <div className={styles.wrapper}>
      <label className={styles.label} htmlFor="sdk-version-select">
        SDK version
      </label>
      <select
        id="sdk-version-select"
        className={styles.select}
        value={activeDocContext.activeVersion.name}
        onChange={handleChange}
      >
        {options.map((option) => (
          <option key={option.name} value={option.name}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}
