import React from 'react';
import {useHistory} from '@docusaurus/router';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const VERSION_OPTIONS = [
  {
    id: 'v2',
    label: 'SDK v2 (latest preview)',
    basePath: '/sdk/v2_dev',
  },
  {
    id: 'v1',
    label: 'SDK v1 (stable)',
    basePath: '/sdk',
  },
];

const PAGE_PATHS = {
  api: '/api',
  mainboard: '/api/mainboard',
  result: '/api/result',
};

export default function SdkApiVersionDropdown({page = 'api', current = 'v1'}) {
  const history = useHistory();
  const pagePath = PAGE_PATHS[page] || '';

  const options = VERSION_OPTIONS.map((version) => ({
    ...version,
    url: useBaseUrl(`${version.basePath}${pagePath}`),
  }));

  const selected = options.find((option) => option.id === current) || options[0];
  const selectId = `sdk-version-${page}`;

  const handleChange = (event) => {
    history.push(event.target.value);
  };

  return (
    <div className={styles.wrapper}>
      <label className={styles.label} htmlFor={selectId}>
        SDK version
      </label>
      <select
        id={selectId}
        className={styles.select}
        value={selected.url}
        onChange={handleChange}
      >
        {options.map((option) => (
          <option key={option.id} value={option.url}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}
