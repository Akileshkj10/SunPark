import type { Metadata } from "next";
import type { ReactNode } from "react";
import { PageShell } from "@/components/PageShell";
import { siteMeta } from "@/content/site";
import "@fontsource/inter/400.css";
import "@fontsource/inter/500.css";
import "@fontsource/inter/600.css";
import "@/styles/components.css";

export const metadata: Metadata = {
  title: {
    default: "SunPark | Solar carports without upfront capex",
    template: "%s | SunPark",
  },
  description: siteMeta.description,
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <PageShell>{children}</PageShell>
      </body>
    </html>
  );
}
