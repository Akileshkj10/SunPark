import Link from "next/link";
import type { AnchorHTMLAttributes, ButtonHTMLAttributes, ReactNode } from "react";
import { classNames } from "@/lib/classNames";

type ButtonVariant = "primary" | "secondary" | "secondaryOnDark";

type CommonProps = {
  children: ReactNode;
  className?: string;
  variant?: ButtonVariant;
};

type ButtonAsLink = CommonProps &
  AnchorHTMLAttributes<HTMLAnchorElement> & {
    href: string;
  };

type ButtonAsButton = CommonProps &
  ButtonHTMLAttributes<HTMLButtonElement> & {
    href?: never;
  };

export type ButtonProps = ButtonAsLink | ButtonAsButton;

const variantClass: Record<ButtonVariant, string> = {
  primary: "button--primary",
  secondary: "button--secondary",
  secondaryOnDark: "button--secondary-on-dark",
};

export function Button({
  children,
  className,
  variant = "primary",
  ...props
}: ButtonProps) {
  const buttonClassName = classNames("button", variantClass[variant], className);

  if (typeof (props as ButtonAsLink).href === "string") {
    const { href, ...anchorProps } = props as ButtonAsLink;

    return (
      <Link className={buttonClassName} href={href} {...anchorProps}>
        {children}
      </Link>
    );
  }

  const buttonProps = props as ButtonAsButton;

  return (
    <button className={buttonClassName} {...buttonProps}>
      {children}
    </button>
  );
}
