import type { ElementType, ReactNode } from "react";
import { classNames } from "@/lib/classNames";

type SectionShellProps = {
  as?: ElementType;
  children: ReactNode;
  className?: string;
  compact?: boolean;
  id?: string;
};

export function SectionShell({
  as: Component = "section",
  children,
  className,
  compact = false,
  id,
}: SectionShellProps) {
  return (
    <Component
      className={classNames(
        "section-shell",
        compact && "section-shell--compact",
        className,
      )}
      id={id}
    >
      {children}
    </Component>
  );
}
