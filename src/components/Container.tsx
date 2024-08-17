interface ContainerProps {
  as?: React.ElementType;
  children: React.ReactNode;
  className?: string;
}

export const Container = ({
  as: Element = "div",
  children,
  className,
  ...rest
}: ContainerProps) => {
  return (
    <Element
      {...rest}
      className={`flex flex-col w-full max-w-screen h-screen m-auto bg-mac-grey ${className}`}
    >
      {children}
    </Element>
  );
};
