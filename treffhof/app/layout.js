import './globals.css'
import { Inter } from 'next/font/google'
import Script from 'next/script'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'TreffHOF',
  description: 'Treffneri Hall of Fame',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">

      <Script
        src="https://www.googletagmanager.com/gtag/js?id=G-FMQ3QR4NR6"
        strategy="afterInteractive"
      />
      <Script id="google-analytics" strategy="afterInteractive">
        {`
          window.dataLayer = window.dataLayer || [];
          function gtag(){window.dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'G-FMQ3QR4NR6');
        `}
      </Script>

      <body className={inter.className}>{children}</body>
    </html>
  )
}
