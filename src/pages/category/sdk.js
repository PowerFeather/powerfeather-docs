import React, {useEffect} from 'react';
import Head from '@docusaurus/Head';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function SdkCategoryRedirect() {
  const sdkUrl = useBaseUrl('/sdk');

  useEffect(() => {
    window.location.replace(sdkUrl);
  }, [sdkUrl]);

  return (
    <>
      <Head>
        <title>SDK | PowerFeather Docs</title>
        <link rel="canonical" href={sdkUrl} />
        <meta httpEquiv="refresh" content={`0; url=${sdkUrl}`} />
      </Head>
      <main className="container margin-vert--lg">
        <h1>SDK</h1>
        <p>
          Redirecting to <a href={sdkUrl}>the SDK documentation</a>.
        </p>
      </main>
    </>
  );
}
