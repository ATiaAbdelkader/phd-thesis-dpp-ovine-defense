import type { Metadata } from "next";
import { Playfair_Display, Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";

const playfair = Playfair_Display({
  variable: "--font-heading",
  subsets: ["latin"],
  weight: ["400", "700", "900"],
});

const inter = Inter({
  variable: "--font-body",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800"],
});

const jetbrains = JetBrains_Mono({
  variable: "--font-num",
  subsets: ["latin"],
  weight: ["400", "500", "700"],
});

export const metadata: Metadata = {
  title: "PhD Defense — Date Palm Pollen for Ovine Genetic Rescue",
  description: "Interactive PhD thesis defense presentation. Date Palm Pollen (Phoenix dactylifera L.) as a Natural Cryoprotective Agent for Post-Slaughter Ovine Epididymal Sperm Preservation.",
  keywords: ["PhD thesis", "Date Palm Pollen", "Ovine", "Epididymal Sperm", "Genetic Conservation", "Algeria", "El Oued", "Ouled Djellal"],
  authors: [{ name: "[Candidate Name]" }],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${playfair.variable} ${inter.variable} ${jetbrains.variable} antialiased bg-background text-foreground`}
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
