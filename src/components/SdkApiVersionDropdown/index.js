import React from 'react';
import {useHistory} from '@docusaurus/router';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const VERSION_OPTIONS = [
  {
    id: '2.x',
    label: '2.x (preview)',
    basePath: '/sdk/2.x',
  },
  {
    id: '1.x',
    label: '1.x',
    basePath: '/sdk/1.x',
  },
];

const PAGE_PATHS = {
  api: '/api',
  mainboard: '/api/mainboard',
  result: '/api/result',
  setup: '/setup',
};

export default function SdkApiVersionDropdown({page = 'api', current = '2.x'}) {
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
        SDK Version
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
