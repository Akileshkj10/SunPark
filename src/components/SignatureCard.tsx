import type { ReactNode } from "react";
import { classNames } from "@/lib/classNames";

type SignatureTone = "coral" | "forest" | "dark" | "cream";

type SignatureCardProps = {
  children: ReactNode;
  className?: string;
  tone?: SignatureTone;
};

export function SignatureCard({
  children,
  className,
  tone = "forest",
}: SignatureCardProps) {
  return (
    <div className={classNames("signature-card", `signature-card--${tone}`, className)}>
      {children}
    </div>
  );
}
