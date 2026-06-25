import type { ReactNode } from "react";
import { classNames } from "@/lib/classNames";

type ResponsiveGridProps = {
  children: ReactNode;
  className?: string;
  columns?: 2 | 3;
};

export function ResponsiveGrid({
  children,
  className,
  columns = 3,
}: ResponsiveGridProps) {
  return (
    <div
      className={classNames(
        "section-grid",
        columns === 2 ? "section-grid--two" : "section-grid--three",
        className,
      )}
    >
      {children}
    </div>
  );
}
